from nose.tools import *
from ex48 import lexicon
from ex48 import parserb

def test_sentence_obj():
	s = parserb.Sentence(('noun', 'princess'), ('verb', 'go'), ('number', 3), ('object', 'south'))
	assert_equal(s.subject, 'princess')
	assert_equal(s.verb, 'go')
	assert_equal(s.number, 3)
	assert_equal(s.object, 'south')
	assert_equal(s.to_tuple(), ('princess', 'go', 3, 'south'))
	
def test_peek():
	word_list = lexicon.scan('princess')
	assert_equal(parserb.peek(word_list), 'noun')
	assert_equal(parserb.peek(None), None)
	
def test_match():
	word_list = lexicon.scan('princess')
	assert_equal(parserb.match(word_list, 'noun'), ('noun', 'princess'))
	assert_equal(parserb.match(word_list, 'stop'), None)
	assert_equal(parserb.match(None, 'noun'), None)
	
def test_skip():
    word_list = lexicon.scan('princess go north')
    parserb.skip(word_list, 'noun')
    assert_equal(word_list, [('verb', 'go'), ('direction', 'north')])
	
def test_parse_verb():
	word_list = lexicon.scan('in eat door')
	assert_equal(parserb.parse_verb(word_list), ('verb', 'eat'))
	word_list = lexicon.scan('bear eat door')
	assert_raises(parserb.ParserbError, parserb.parse_verb, word_list)
	
def test_parse_number():
	word_list = lexicon.scan('of 3 bear')
	assert_equal(parserb.parse_number(word_list), ('number', 3))
	word_list = lexicon.scan('bear eat 3 door')
	assert_equal(parserb.parse_number(word_list), ('number', 1))
	
def test_parse_object():
	word_list = lexicon.scan('the door')
	assert_equal(parserb.parse_object(word_list), ('noun', 'door'))
	word_list = lexicon.scan('of east')
	assert_equal(parserb.parse_object(word_list), ('direction', 'east'))
	word_list = lexicon.scan('the in')
	assert_raises(parserb.ParserbError, parserb.parse_object, word_list)
	
def test_parse_subject():
	word_list = lexicon.scan('eat 3 door')
	subj = ('noun', 'princess')
	s = parserb.parse_subject(word_list, subj)
	assert_equal(s.to_tuple(), ('princess', 'eat', 3, 'door'))

def test_parse_sentence():
	word_list = lexicon.scan('the bear go 3 door')
	s = parserb.parse_sentence(word_list)
	assert_equal(s.to_tuple(), ('bear', 'go', 3, 'door'))
	word_list = lexicon.scan('the go 3 door')
	s = parserb.parse_sentence(word_list)
	assert_equal(s.to_tuple(), ('player', 'go', 3, 'door'))
	word_list = lexicon.scan('north go door')
	s = parserb.parse_sentence(word_list)
	assert_raises(parserb.ParserbError, parserb.parse_sentence, word_list)
	
def test_unknown_words():
	word_list = lexicon.scan('xxx the xxxx bear xxxx go xxxx 3 xxxx door')
	s = parserb.parse_sentence(word_list)
	assert_equal(s.to_tuple(), ('bear', 'go', 3, 'door'))
	
	
