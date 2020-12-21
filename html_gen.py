import os
frame = ['<!DOCTYPE html>\n', '<html>\n', '<head>\n', '\t<title><title>\n', '</head>\n','<body>\n', '', '</body>\n', '</html>\n']
supported_tags = ('img','div','a','button','input','h1','hr','p','i','strong')

class Generator():

	def __init__(self):
		pass

	def FillTemplate(self, head, body):
		title, meta, link = head
		self.__FillHead(title = title, meta = meta, link = link)
		self.__FillBody(body)

	def InitTemplate(self):

		self.template = Template(frame)

	def __FillHead(self, title = '', meta = [], link = []):

		self.__FillTitle(title)
		self.__FillMeta(meta)
		self.__FillLink(link)


	def __FillTitle(self, title):

		file = open('Template/index.html', 'r')
		data = file.readlines()
		file.close()
		file = open('Template/index.html', 'w')
		data[data.index('\t<title><title>\n')] = '\t<title>{0}<title>\n'.format(title)
		file.writelines(data)
		file.close()

	def __FillMeta(self, meta):

		file = open('Template/index.html', 'r')
		data = file.readlines()
		file.close()
		file = open('Template/index.html', 'w')
		for i in range(len(meta)):
			data.insert(data.index('</head>\n'), '\t<meta charset = \'{0}\' name = \'{1}\' content = \'{2}\'>\n'.format(meta[i][0], meta[i][1], meta[i][2]))
		file.writelines(data)
		file.close()

	def __FillLink(self, link):

		file = open('Template/index.html', 'r')
		data = file.readlines()
		file.close()
		file = open('Template/index.html', 'w')
		for i in range(len(link)):
			data.insert(data.index('</head>\n'), '\t<link rel = \'{0}\' type = \'{1}\' href = \'{2}\' media = \'{3}\'>\n'.format(link[i][0], link[i][1], link[i][2], link[i][3]))
		file.writelines(data)
		file.close()

	def __FillBody(self, body):
		
		file = open('Template/index.html', 'r')
		data = file.readlines()
		file.close()
		file = open('Template/index.html', 'w')

		for i in range(len(body)):
			is_first_eterate = True
			if body[i][0].forename == 'img' or body[i][0].forename == 'a' or body[i][0].forename == 'hr':
				div_nesting = body[i][1]
				while div_nesting >= 1:
					is_first_eterate = False
					if body[i][0].forename == 'img':
						if div_nesting == body[i][1]:
							data.insert(data.index('<body>\n')+1, (int(div_nesting) + 1)*'\t'+'\n<{0} src = \'{1}\'>\n'.format(body[i][0].forename, body[i][0].src))
						data.insert(data.index('<body>\n')+1, int(div_nesting)*'\t'+'<div>')
						data.insert(data.index('</body>\n'), int(div_nesting)*'\t'+'</div>\n')
						div_nesting -= 1
					elif body[i][0].forename == 'a':
						if div_nesting == body[i][1]:
							data.insert(data.index('<body>\n')+1, (int(div_nesting) + 1)*'\t'+'\n<{0} href = \'{1}\'>ClickMe</{0}>\n'.format(body[i][0].forename, body[i][0].href))
						data.insert(data.index('<body>\n')+1, int(div_nesting)*'\t'+'<div>')
						data.insert(data.index('</body>\n'), int(div_nesting)*'\t'+'</div>\n')
						div_nesting -= 1
					elif body[i][0].forename == 'hr':
						if div_nesting == body[i][1]:
							data.insert(data.index('<body>\n')+1, (int(div_nesting) + 1)*'\t'+'\n</{0}>\n'.format(body[i][0].forename))
						data.insert(data.index('<body>\n')+1, int(div_nesting)*'\t'+'<div>')
						data.insert(data.index('</body>\n'), int(div_nesting)*'\t'+'</div\n>')
						div_nesting -= 1
				if div_nesting == 0 and is_first_eterate == True:
					if body[i][0].forename == 'img':
						data.insert(data.index('<body>\n')+1, (int(div_nesting) + 1)*'\t'+'\n<{0} src = \'{1}\'>\n'.format(body[i][0].forename, body[i][0].src))
					elif body[i][0].forename == 'a':
						data.insert(data.index('<body>\n')+1, (int(div_nesting) + 1)*'\t'+'\n<{0} href = \'{1}\'>ClickMe</{0}>\n'.format(body[i][0].forename, body[i][0].href))
					elif body[i][0].forename == 'hr':
						data.insert(data.index('<body>\n')+1, (int(div_nesting) + 1)*'\t'+'\n</{0}>\n'.format(body[i][0].forename))
			else:
				div_nesting = body[i][1]
				while div_nesting >= 1:
					is_first_eterate = False
					if body[i][0].forename == 'div':
						if div_nesting == body[i][1]:
							data.insert(data.index('<body>\n')+1, (int(div_nesting) + 1)*'\t'+'\n<{0}></{0}>\n'.format(body[i][0].forename))
						data.insert(data.index('<body>\n')+1, int(div_nesting)*'\t'+'<div>')
						data.insert(data.index('</body>\n'), int(div_nesting)*'\t'+'</div>\n')
						div_nesting -= 1
					elif body[i][0].forename == 'button':
						if div_nesting == body[i][1]:
							data.insert(data.index('<body>\n')+1, '{1}\n<{0}>ClickMe</{0}>\n'.format(body[i][0].forename, ((int(div_nesting) + 1)*'\t')))
						data.insert(data.index('<body>\n')+1, int(div_nesting)*'\t'+'<div>')
						data.insert(data.index('</body>\n'), int(div_nesting)*'\t'+'</div>\n')
						div_nesting -= 1
					elif body[i][0].forename == 'input':
						if div_nesting == body[i][1]:
							data.insert(data.index('<body>\n')+1, (int(div_nesting) + 1)*'\t'+'\n<{0} type = \'{1}\'>Some Text</{0}>\n'.format(body[i][0].forename))
						data.insert(data.index('<body>\n')+1, int(div_nesting)*'\t'+'<div>')
						data.insert(data.index('</body>\n'), int(div_nesting)*'\t'+'</div>\n')
						div_nesting -= 1
					elif body[i][0].forename == 'h1':
						if div_nesting == body[i][1]:
							data.insert(data.index('<body>\n')+1, (int(div_nesting) + 1)*'\t'+'\n<{0}>Some Text</{0}>\n'.format(body[i][0].forename))
						data.insert(data.index('<body>\n')+1, int(div_nesting)*'\t'+'<div>')
						data.insert(data.index('</body>\n'), int(div_nesting)*'\t'+'</div>\n')
						div_nesting -= 1
					elif body[i][0].forename == 'i':
						if div_nesting == body[i][1]:
							data.insert(data.index('<body>\n')+1, (int(div_nesting) + 1)*'\t'+'\n<{0}>Some Text</{0}>\n'.format(body[i][0].forename))
						data.insert(data.index('<body>\n')+1, int(div_nesting)*'\t'+'<div>')
						data.insert(data.index('</body>\n'), int(div_nesting)*'\t'+'</div>\n')
						div_nesting -= 1
					elif body[i][0].forename == 'p':
						if div_nesting == body[i][1]:
							data.insert(data.index('<body>\n')+1, (int(div_nesting) + 1)*'\t'+'\n<{0}>Some Text</{0}>\n'.format(body[i][0].forename))
						data.insert(data.index('<body>\n')+1, int(div_nesting)*'\t'+'<div>')
						data.insert(data.index('</body>\n'), int(div_nesting)*'\t'+'</div>\n')
						div_nesting -= 1
					elif body[i][0].forename == 'strong':
						if div_nesting == body[i][1]:
							data.insert(data.index('<body>\n')+1, (int(div_nesting) + 1)*'\t'+'\n<{0}>Some Text</{0}>\n'.format(body[i][0].forename))
						data.insert(data.index('<body>\n')+1, int(div_nesting)*'\t'+'<div>')
						data.insert(data.index('</body>\n'), int(div_nesting)*'\t'+'</div>\n')
						div_nesting -= 1
				if div_nesting == 0 and is_first_eterate == True:
					if body[i][0].forename == 'div':
						data.insert(data.index('<body>\n')+1, (int(div_nesting) + 1)*'\t'+'\n<{0}></{0}>\n'.format(body[i][0].forename))
					elif body[i][0].forename == 'button':
						data.insert(data.index('<body>\n')+1, (int(div_nesting) + 1)*'\t'+'\n<{0}>ClickMe</{0}>\n'.format(body[i][0].forename))
					elif body[i][0].forename == 'input':
						data.insert(data.index('<body>\n')+1, (int(div_nesting) + 1)*'\t'+'\n<{0} type = \'{1}\'>Some Text</{0}>\n'.format(body[i][0].forename, body[i][0].type))
					elif body[i][0].forename == 'h1':
						data.insert(data.index('<body>\n')+1, (int(div_nesting) + 1)*'\t'+'\n<{0}>Some Text</{0}>\n'.format(body[i][0].forename))
					elif body[i][0].forename == 'i':
						data.insert(data.index('<body>\n')+1, (int(div_nesting) + 1)*'\t'+'\n<{0}>Some Text</{0}>\n'.format(body[i][0].forename))
					elif body[i][0].forename == 'p':
						data.insert(data.index('<body>\n')+1, (int(div_nesting) + 1)*'\t'+'\n<{0}>Some Text</{0}>\n'.format(body[i][0].forename))
					elif body[i][0].forename == 'strong':
						data.insert(data.index('<body>\n')+1, (int(div_nesting) + 1)*'\t'+'\n<{0}>Some Text</{0}>\n'.format(body[i][0].forename))
		file.writelines(data)
		file.close()

class Template():

	def __init__(self, sequence_frames_strings):
		self.__Generate_Frame(sequence_frames_strings)

	def __Generate_Frame(self, frames_sequence):
		html_frame = open('Template/index.html','w')
		try:
			html_frame.writelines(frames_sequence)
			html_frame.close()
		except:
			html_frame.close()

class UserManager():

	div_nesting = 0
	def AskUsersWishes(self):
		head = input('Would you like to fill <head> (yes or no)? ')
		body = input('Would you like to fill <body> (yes or no)? ')
		print('\n')
		build_head_preferences, build_body_preferences = self.__AskUsersPreferences(head = head, body = body)
		return [build_head_preferences, build_body_preferences]

	def __AskUsersPreferences(self, head, body):

		try:
			if head.lower() == 'yes':
				head_preferences = []
				head_preferences = self.__AskHeadPreferences()
			elif head.lower() != 'no':
				raise ValueError
		except ValueError as error:
			print('You Entered invalid value')

		try:
			if body.lower() == 'yes':
				body_preferences = []
				body_preferences = self.__AskBodyPreferences()
			elif head.lower() != 'no':
				raise ValueError
		except ValueError as error:
			print('You Entered invalid value')

		return [head_preferences, body_preferences]

	def __AskHeadPreferences(self):

		meta = []
		title = input('Enter title of head: ')
		count_meta_tags = input('How many meta tags will be in page? ')
		print('\n')
		try:
			count_meta_tags = int(count_meta_tags)
		except:
			raise ValueError
		meta_eterate = []
		if count_meta_tags != 0:
			for i in range(count_meta_tags):
				meta_charset = input('Enter \'charset\' parametr: ')
				meta_name = input('Enter \'name\' parametr: ')
				meta_content = input('Enter \'content\' parametr: ')
				meta_eterate.append([meta_charset.lower(), meta_name.lower(), meta_content.lower()])
		print('\n')		
		count_link_tags = input('How many link tags will be in page?')
		try:
			count_link_tags = int(count_link_tags)
		except:				
			raise ValueError
		link_eterate = []
		if count_link_tags != 0:
			for i in range(count_link_tags):
				link_rel = input('Enter \'rel\' parametr: ')
				link_type = input('Enter \'type\' parametr: ')
				link_href = input('Enter \'href\' parametr: ')
				link_media =  input('Enter \'media\' parametr: ')
				link_eterate.append([link_rel.lower(), link_type.lower(), link_href.lower(), link_media.lower()])
		print('\n')
		return [title, meta_eterate, link_eterate]

	def __AskBodyPreferences(self):

		body = []
		print('Supported tags:')
		for tag in supported_tags:
			print(tag)
		print('\n')

		count_element = input('How many tags will be in <body> ? ')
		print('\n')
		try:
			count_element = int(count_element)
		except ValueError:
			raise ValueError
		for i in range(count_element):
			body_element = self.__GetElement()
			body.append(body_element)

		return body

	def __GetElement(self):
		element_type = input('Which tag do you want to insert: ')
		print('\n')
		body_element = self.__InitElement(element_type)
		try:
			int(body_element)
			raise ValueError
		except:
			pass

		self.__GetDivNesting()
		return [body_element, self.div_nesting]


	def __GetDivNesting(self):

		if self.div_nesting != 0:
			again = 'again'
		else:
			again = ''
		is_div_exist = input('Will be your element wrapped {0} in <div>? '.format(again))
		try:
			if is_div_exist.lower() == 'yes':
				self.div_nesting += 1
				self.__GetDivNesting()
		except:
			return 0
		return 0

	def __InitElement(self, type):

		try:
			assert (type in supported_tags)
		except:
			print('Error: Unsupported tag')
			raise AssertionError

		if type == 'img':
			element = img()
		elif type == 'a':
			element = a()
		elif type == 'h1':
			element = h1()
		elif type == 'div':
			element = div()
		elif type == 'input':
			element = input_t()
		elif type == 'button':
			element = button()
		elif type == 'hr':
			element = hr()
		elif type == 'p':
			element = p()
		elif type == 'i':
			element = i()
		elif type == 'strong':
			element = strong()
		return element

class img():

	def __init__(self, src = 'media/img.png', forename = 'img'):
		self.src = src
		self.img = img

class a():

	def __init__(self, href = 'google.com', forename = 'a'):
		self.href = href
		self.forename = forename

class h1():

	def __init__(self, forename = 'h1'):
		self.forename = forename

class div():

	def __init__(self, forename = 'div'):
		self.forename = forename

class input_t():

	def __init__(self, type_f='text', name='text', value='', forename = 'input'):
		self.type = type_f
		self.name = name
		self.value = value
		self.forename = forename

class button():

	def __init__(self, forename = 'button'):
		self.forename = forename

class hr():

	def __init__(self, forename = 'hr'):
		self.forename = forename

class p():

	def __init__(self, forename = 'p'):
		self.forename = forename

class i():

	def __init__(self, forename = 'i'):
		self.forename = forename

class strong():

	def __init__(self, forename = 'strong'):
		self.forename = forename


html_generator = Generator()
html_generator.InitTemplate()
manager = UserManager()
head_wishes, body_wishes = manager.AskUsersWishes()
html_generator.FillTemplate(head_wishes, body_wishes)