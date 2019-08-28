' url handlers '

import re, time, json, logging, hashlib, base64, asyncio

from coreweb import get, post
from models import User, Comment, Blog, next_id

@get('/')
async def index(request):
	users = await User.findAll()
	if users is None:
		users = []
	return {
		'__template__': 'test.html',
		'users': users
	}


