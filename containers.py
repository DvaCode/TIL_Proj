# containers.py
from ulid import ULID
from utils.crypto import Crypto
from user.application.send_welcome_email_task import SendWelcomeEmailTask
from dependency_injector import containers, providers
from user.infra.repository.user_repo import UserRepository
from user.application.user_service import UserService
from note.application.note_service import NoteService
from note.infra.repository.note_repo import NoteRepository
from fastapi import BackgroundTasks
from user.application.email_service import EmailService

class Container(containers.DeclarativeContainer):
    
    wiring_config = containers.WiringConfiguration(
        packages=["user"],
    )
    user_repo = providers.Factory(UserRepository)
    user_service = providers.Factory(UserService, user_repo=user_repo)
    note_repo = providers.Factory(NoteRepository)
    note_service = providers.Factory(NoteService, note_repo=note_repo)
    ulid = providers.Factory(ULID)
    crypto = providers.Factory(Crypto)
    send_welcome_email_task = providers.Factory(SendWelcomeEmailTask)
    email_service = providers.Factory(EmailService)
    user_service = providers.Factory(
        UserService,
        user_repo = user_repo,
        email_service = email_service,
        ulid = ulid,
        crypto = crypto,
        send_welcome_email_task = send_welcome_email_task,
    )