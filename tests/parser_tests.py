from nose.tools import *
from ex48 import lexicon
from ex48 import parser

def test_sentence_obj():
	s = parser.Sentence(('noun', 'princess'), ('verb', 'go'), ('object', 'south'))
	assert_equal(s.subject, 'princess')
	assert_equal(s.verb, 'go')
	assert_equal(s.object, 'south')
	assert_equal(s.to_tuple(), ('princess', 'go', 'south'))
	
def test_peek():
	word_list = lexicon.scan('princess')
	assert_equal(parser.peek(word_list), 'noun')
	assert_equal(parser.peek(None), None)
	
def test_match():
	word_list = lexicon.scan('princess')
	assert_equal(parser.match(word_list, 'noun'), ('noun', 'princess'))
	assert_equal(parser.match(word_list, 'stop'), None)
	assert_equal(parser.match(None, 'noun'), None)
	
def test_skip():
    word_list = lexicon.scan('princess go north')
    parser.skip(word_list, 'noun')
    assert_equal(word_list, [('verb', 'go'), ('direction', 'north')])
	
def test_parse_verb():
	word_list = lexicon.scan('in eat door')
	assert_equal(parser.parse_verb(word_list), ('verb', 'eat'))
	word_list = lexicon.scan('bear eat door')
	assert_raises(parser.ParserError, parser.parse_verb, word_list)
	
def test_parse_object():
	word_list = lexicon.scan('the door')
	assert_equal(parser.parse_object(word_list), ('noun', 'door'))
	word_list = lexicon.scan('of east')
	assert_equal(parser.parse_object(word_list), ('direction', 'east'))
	word_list = lexicon.scan('the in')
	assert_raises(parser.ParserError, parser.parse_object, word_list)
	
def test_parse_subject():
	word_list = lexicon.scan('eat door')
	subj = ('noun', 'princess')
	s = parser.parse_subject(word_list, subj)
	assert_equal(s.to_tuple(), ('princess', 'eat', 'door'))

def test_parse_sentence():
	word_list = lexicon.scan('the bear go door')
	s = parser.parse_sentence(word_list)
	assert_equal(s.to_tuple(), ('bear', 'go', 'door'))
	word_list = lexicon.scan('the go door')
	s = parser.parse_sentence(word_list)
	assert_equal(s.to_tuple(), ('player', 'go', 'door'))
	word_list = lexicon.scan('north go door')
	s = parser.parse_sentence(word_list)
	assert_raises(parser.ParserError, parser.parse_sentence, word_list)
	
def test_unknown_words():
	word_list = lexicon.scan('xxx the xxxx bear xxxx go xxxx door')
	s = parser.parse_sentence(word_list)
	assert_equal(s.to_tuple(), ('bear', 'go', 'door'))
	
	
