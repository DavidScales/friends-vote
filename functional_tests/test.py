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

  def test_user_can_create_poll(self):

    # Susan is wasting time on the internet and accidentally opens the
    # home page of Friends Vote
    self.browser.get(self.live_server_url)

    ## Sanity check
    # She sees that the page title and header mention friends and voting
    self.assertEqual('Friends Vote', self.browser.title)
    header_text = self.browser.find_element_by_tag_name('h1').text
    self.assertIn('Friends Vote', header_text)

    self.fail('Expected failure: Finish the test!')

    # and that there is some text prompting her to create a new poll for
    # her friends to vote on

    # She sees a single text box for creating a poll question

    # She types "What pet should I get?" into the text box

    # When she hits enter, two new text boxes appear, prompting her
    # for answers to her question

    # She types "a cat" into the first box

    # and "a dog" into the second box

    # She sees that there is a button for adding more answers

    # When she clicks it, a third text box appears

    # She types "a lizard" into the third box

    # Though she is satisfied with her answers for now, she takes not that
    # the button for adding more answers is still there

    # She sees text telling her to press enter when she's finished

    # When she presses enter, she is redirected to a new page, and she
    # notices that the page contains a unique URL (vote)

        ## What if she has 5 answer boxes but only 3 have text when she submits?
        ## What if she doesn't submit any text, or only text for one answer?

    # The page content has text that contains her question/poll

    # The page also contains her answers as radio input choices

    # She chooses the third answer, "a lizard", and text appears prompting her to
    # press enter when she is ready to cast her vote

    # When she presses enter, she is redirected to a new page and she notices that
    # the page again contains a unique URL (results)

        ## What if she tries to submit without choosing an answer (front end and back end)

    # The page displays her question in a heading

    # as well as each of the possible answers as list items

    # Next to each answer is a vote count

    # and a vote percentage


## new class - others can vote on a poll
# Susan shares her voting URL...

## new class - others can view poll results
# Susan shares her results URL...