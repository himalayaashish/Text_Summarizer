from transformers import pipeline

# Using GPU if available and cleaning up tokenization spaces
summarizer = pipeline("summarization", model="lidiya/bart-large-xsum-samsum", clean_up_tokenization_spaces=True, device=0)

conversation = '''
TIME: I wanted to begin in the news. Iran overnight said it was considering enriching uranium at
      levels that would violate the 2015 nuclear agreement.
      You’ve been very clear that you won’t let Iran get a nuclear weapon.

TRUMP: Yeah, I think they’d be making a big mistake doing that.

TIME: Are you considering more military action?

TRUMP: I wouldn’t say that. I can’t say that at all. It would be inappropriate. But they would be making a big mistake if they enriched.

TIME: Are they calling your bluff on this or how do you see it?

TRUMP: Time will tell. Only time will tell.

TIME: I mean in your campaign, you promised to get the U.S. out of unnecessary foreign wars. With your —

TRUMP: That’s true. Well I have.
'''

# Summarizing the conversation
summary = summarizer(conversation)[0]['summary_text']
print(summary)
