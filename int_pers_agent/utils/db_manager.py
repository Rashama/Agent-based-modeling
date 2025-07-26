# db_manager.py
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
import logging

# Configure database URI
DATABASE_URI = "postgresql://postgres:Gakhar555@database-3.cl8ugeouejun.eu-north-1.rds.amazonaws.com:5432/postgres"

# Create engine and session
engine = create_engine(DATABASE_URI)
SessionLocal = scoped_session(sessionmaker(bind=engine))

# Base class for models
Base = declarative_base()

# Setup logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Define Idea model
class Idea(Base):
    __tablename__ = "idea"

    id = Column(Integer, primary_key=True, index=True)
    main_idea = Column(String(200), nullable=True)
    resubmitted_idea = Column(String(200), nullable=True)
    agent_name = Column(String(100), nullable=True)
    generative_num = Column(Integer, nullable=True)

    def __repr__(self):
        return f"<Idea {self.id} - {self.main_idea} - {self.resubmitted_idea} - {self.agent_name} - {self.generative_num}>"

# Create all tables
def create_tables():
    try:
        Base.metadata.create_all(bind=engine)
        logger.info("✅ Tables created successfully.")
    except Exception as e:
        logger.error(f"❌ Error creating tables: {e}")
        raise

# Insert a blank row and return the new ID
def create_user_slot():
    session = SessionLocal()
    try:
        blank_idea = Idea()
        session.add(blank_idea)
        session.commit()
        session.refresh(blank_idea)
        logger.info(f"✅ Blank idea created with ID: {blank_idea.id}")
        return blank_idea.id
    except Exception as e:
        session.rollback()
        logger.error(f"❌ Error creating user slot: {e}")
        raise
    finally:
        session.close()

# Update or insert idea by ID
def update_idea_by_id(idea_id, main_idea=None, resubmitted_idea=None, agent_name=None):
    session = SessionLocal()
    try:
        idea = session.get(Idea, idea_id)

        if idea:
            if main_idea is not None:
                idea.main_idea = main_idea
            if resubmitted_idea is not None:
                idea.resubmitted_idea = resubmitted_idea
            if agent_name is not None:
                idea.agent_name = agent_name
            logger.info(f"✅ Idea ID {idea_id} updated.")
        else:
            idea = Idea(
                id=idea_id,
                main_idea=main_idea,
                resubmitted_idea=resubmitted_idea,
                agent_name=agent_name
            )
            session.add(idea)
            logger.info(f"✅ New idea created with ID {idea_id}.")

        session.commit()
    except Exception as e:
        session.rollback()
        logger.error(f"❌ Error updating idea ID {idea_id}: {e}")
        raise
    finally:
        session.close()

# Update generative number by ID
def update_generative_num_by_id(idea_id, num):
    session = SessionLocal()
    try:
        idea = session.get(Idea, idea_id)
        if idea:
            idea.generative_num = num
            session.commit()
            logger.info(f"✅ Updated generative_num for idea ID {idea_id} to {num}")
        else:
            logger.warning(f"⚠️ Idea ID {idea_id} not found.")
    except Exception as e:
        session.rollback()
        logger.error(f"❌ Error updating generative_num for idea ID {idea_id}: {e}")
        raise
    finally:
        session.close()

# For standalone testing
if __name__ == "__main__":
    create_tables()
