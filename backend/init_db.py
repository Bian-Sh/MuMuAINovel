#!/usr/bin/env python3
"""Initialize SQLite database tables synchronously."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
os.chdir(os.path.dirname(__file__))

from dotenv import load_dotenv
load_dotenv('.env')

from app.database import Base
from app.models import (
    Project, Outline, Character, Chapter, GenerationHistory,
    Settings, WritingStyle, ProjectDefaultStyle,
    RelationshipType, CharacterRelationship, Organization, OrganizationMember,
    StoryMemory, PlotAnalysis, AnalysisTask, BatchGenerationTask,
    RegenerationTask, Career, CharacterCareer, User, MCPPlugin, PromptTemplate
)
from sqlalchemy import create_engine

db_path = os.path.join(os.path.dirname(__file__), 'data', 'ai_story.db')
os.makedirs(os.path.dirname(db_path), exist_ok=True)

engine = create_engine(f'sqlite:///{db_path}', echo=False)
Base.metadata.create_all(engine)

print(f"Tables created in: {db_path}")
print("Tables:", list(Base.metadata.tables.keys()))
