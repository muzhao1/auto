#!/usr/bin/env python
#-*- coding: UTF-8 -*- 
#

import logging
import logging.config



class Util(object):
	'''
	工具函数
	'''
	
	@classmethod
	def response(cls, rsm, errno, err):
		return {'rsm':rsm, 'errno':errno, 'err':err}

	@classmethod
	def getLogger():
		logging.config.fileConfig("config/logger.config")
		logger = logging.getLogger("trace")

		return logger
		
		
if __name__ == "__main__":

	rsm = {"url":"/explore"}
	errno = 0
	err = 'succ'
	print Util.response(rsm, errno, err)
