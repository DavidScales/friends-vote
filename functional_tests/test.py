from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
import time

MAX_WAIT = 10

class NewVisitorTest(LiveServerTestCase):

  def setUp(self):
    self.browser = webdriver.Firefox()

  def tearDown(self):
    self.browser.quit()

  def wait_for_elements_by_tag(self, tag_name):
    start_time = time.time()
    while True:
      try:
        elements = self.browser.find_elements_by_tag_name(tag_name)
        return elements
      except (AssertionError, WebDriverException) as e:
        if time.time() - start_time > MAX_WAIT:
          raise e
        time.sleep(0.5)

  def test_user_can_create_poll(self):

    # Susan is wasting time on the internet and accidentally opens the
    # home page of Friends Vote
    self.browser.get(self.live_server_url)

    ## Sanity check
    # She sees that the page title and header mention friends and voting
    self.assertEqual('Friends Vote', self.browser.title)
    header_text = self.browser.find_element_by_tag_name('h1').text
    self.assertIn('Friends Vote', header_text)

    # There is also an accessibly labelled text input prompting her to create
    # a new question for her friends to vote on
    question_label = self.browser.find_elements_by_tag_name('label')[0].text
    self.assertEqual(question_label, 'Enter a question for your friends to vote on:')

    # as well as two other inputs below that, prompting her for possible
    # answers to her question
    answer_label_1 = self.browser.find_elements_by_tag_name('label')[1].text
    self.assertEqual(answer_label_1, 'Answer 1:')
    answer_label_2 = self.browser.find_elements_by_tag_name('label')[2].text
    self.assertEqual(answer_label_2, 'Answer 2:')

    # She types "What pet should I get?" into the text box
    question_input = self.browser.find_element_by_id('question')
    question_input.send_keys('What pet should I get?')

    # and creates two possible answers by entering "a cat" and "a dog" into
    # the two answer inputs
    answer_input_1 = self.browser.find_element_by_id('answer-1')
    answer_input_1.send_keys('a cat')
    answer_input_2 = self.browser.find_element_by_id('answer-2')
    answer_input_2.send_keys('a dog')

    # Then she presses enter
    answer_input_2.send_keys(Keys.ENTER)

    # The page updates, and now contains her question
    question_heading = self.wait_for_elements_by_tag('h2')[0]
    self.assertEquals(question_heading.text, 'What pet should I get?')

    # The page also contains her answers as radio inputs
    answer_input_1 = self.wait_for_elements_by_tag('input')[0]
    self.assertEquals(answer_input_1.type, 'radio')
    self.assertEqual(answer_input_1.text, 'a cat')
    answer_input_2 = self.wait_for_elements_by_tag('input')[1]
    self.assertEquals(answer_input_2.type, 'radio')
    self.assertEqual(answer_input_2.text, 'a dog')

    # She chooses the second answer, "a cat", and presses enter again

    # The page updates again, and displays her question in a heading

    # as well as each of the possible answers as list items

    # Next to each answer is a vote count

    # and a vote percentage

    self.fail('Expected failure: Finish the test!')

  # def test_can_create_and_submit_more_answer_options(self):
  #   self.fail('Expected failure: Finish the test!')
  #   # She sees that there is a button for adding more answers
  #   # When she clicks it, a third text box appears
  #   # She types "a lizard" into the third box

  ## URL flow

  ## What if she has 5 answer boxes but only 3 have text when she submits?
  ## What if she doesn't submit any text, or only text for one answer?
  ## What if she tries to vote/submit without choosing an answer (front end and back end)

## new class - others can vote on a poll
# Susan shares her voting URL...

## new class - others can view poll results
# Susan shares her results URL...