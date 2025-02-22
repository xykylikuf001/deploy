from fastapi import APIRouter

from app.contrib.account.api import api as account_api
from app.contrib.chat.api import api as chat_api
from app.contrib.graph_knowledge.api import api as gk_api
from app.contrib.history.api import api as history_api
from app.contrib.pinecone.api import api as pinecone_api
from app.contrib.protocol.api import api as protocol_api
api = APIRouter()


api.include_router(account_api, tags=["account"])
api.include_router(chat_api, tags=["chat"], prefix="/chat")
api.include_router(gk_api, tags=["graph knowledge"], prefix="/gk")
api.include_router(history_api, tags=["history"], prefix="/history")
api.include_router(pinecone_api, tags=["pinecone"], prefix="/pinecone")
api.include_router(protocol_api, tags=["protocol"], prefix="/protocol")
