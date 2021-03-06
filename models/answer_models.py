# -*-coding=utf8-*-
# your models module write here
import sys
import time
import datetime
sys.path.append("..")
from db.dbSession import BaseModel, DBSession
from sqlalchemy import Column, String, Integer

from sqlalchemy.dialects.mysql import \
        BIGINT, BINARY, BIT, BLOB, BOOLEAN, CHAR, DATE, \
        DATETIME, DECIMAL, DECIMAL, DOUBLE, ENUM, FLOAT, INTEGER, \
        LONGBLOB, LONGTEXT, MEDIUMBLOB, MEDIUMINT, MEDIUMTEXT, NCHAR, \
        NUMERIC, NVARCHAR, REAL, SET, SMALLINT, TEXT, TIME, TIMESTAMP, \
        TINYBLOB, TINYINT, TINYTEXT, VARBINARY, VARCHAR, YEAR


class Answer(BaseModel):
	"""
	Answer model
	"""
	__tablename__ = "answer"

	answer_id = Column(Integer, primary_key = True, nullable = False)	# id 
	question_id = Column(Integer, nullable = False)						# 问题id
	answer_content = Column(TEXT, nullable = False)						# 回答内容
	add_time = Column(Integer, nullable = False)						# 添加时间
	against_count = Column(Integer, nullable = True, default = 0)		# 反对票数
	agree_count = Column(Integer, nullable = False, default = 0)		# 赞同票数
	uid = Column(Integer, nullable = False)								# 发布问题用户id
	comment_count = Column(Integer, nullable = True, default = 0)		# 评论总数
	uninterested_count = Column(Integer, nullable = True, default = 0)	# 感兴趣票数
	thanks_count = Column(Integer, nullable = True, default = 0)		# 感谢票数
	category_id = Column(Integer, nullable = True, default = 0)			# 分类id
	has_attach = Column(TINYINT, nullable = True, default = 0)			# 是否有附件
	ip = Column(BIGINT, nullable = True)								# ip
	force_fold = Column(TINYINT, nullable = True, default = 0)			# 是否折叠
	anonymous = Column(TINYINT, nullable = True, default = 0)			# 是否匿名
	publish_source = Column(String(16), nullable = True)				# 来源

	@classmethod
	def queryByAnswerId(cls, answerId):
		session = DBSession()
		answer = session.query(cls).filter(cls.answer_id == answerId).first()
		print "answer[0].uid", answer.uid
		return answer

	@classmethod
	def queryByQuestionId(cls, questionId):
		session = DBSession()
		answers = session.query(cls).filter(cls.question_id == questionId).all()
		return answers

	@classmethod
	def addAnswer(cls, questionId, answerContent, userId):
		obj = cls(question_id = questionId, answer_content = answerContent, uid = userId, add_time = long(time.time()))
		session = DBSession()
		session.add(obj)
		session.commit()
		session.close()
		return True
	
	@classmethod
	def updateVoteByAnswerId(cls, answer_id, type, against_count, agree_count):
		session = DBSession()
		# 0反对票, 1赞同票
		# if type == '-1' :		
			# print 'update against_count'
			# session.query(cls).filter(cls.answer_id == answer_id).update({cls.against_count:count})
		# elif type == '1' :
			# print 'update agree_count'
			# session.query(cls).filter(cls.answer_id == answer_id).update({cls.agree_count:count})
		session.query(cls).filter(cls.answer_id == answer_id).update({cls.against_count:against_count, cls.agree_count:agree_count})
		session.commit()
		session.close()

if __name__ == "__main__":
	questionId = 1
	answerContent = "hello"
	uid = 1
	# Answer.addAnswer(questionId, answerContent, uid)

	answer = Answer.queryById(30)
	print answer.answer_content
	
	Answer.updateVoteByAnswerId(30, '0', 100, 99)

	# print time.ctime()

	# now = long(time.time())
	# print now
	# str = datetime.datetime.utcfromtimestamp(now)
	# print str
	# strnow = str.strftime("%Y-%m-%d %H:%M:%S")
	# print strnow


