from database import Base
from datetime import datetime
from sqlalchemy import String, DateTime, Text, Table, Column, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship

note_tag_association = Table(
    "Note_Tag",
    Base.metadata,
    Column("note_id", String(36), ForeignKey("Note.id")),
    Column("tag_id", String(36), ForeignKey("Tag.id")),
)

class Note(Base):
    __tablename__ = "Note"

    id = Column(String(36), primary_key=True)
    user_id = Column(String(36), nullable=False, index=True)
    title = Column(String(64), nullable=False)
    content = Column(Text, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    updated_at = Column(
        DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow
    )

    tags = relationship( # SQLAlchemy에서 제공하는 relationship을 통해 다대다 관계 형성, back_populates 옵션을 이용해 노트 객체와 연관된 태그 객체 모두 가져옴
        "Tag",
        secondary=note_tag_association,
        back_populates="notes",
        lazy="joined",
    )

class Tag(Base):
    __tablename__ = "Tag"

    id = Column(String(36), primary_key=True)
    name = Column(String(64), nullable=False, unique=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    updated_at = Column(
        DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow
    )

    notes = relationship( # 다대다 관계
        "Note",
        secondary=note_tag_association,
        back_populates="tags",
        lazy="joined",
    )