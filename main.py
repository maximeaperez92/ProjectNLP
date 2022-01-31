import os
from discord.ext import commands
# from dotenv import load_dotenv
import gpt_2_simple as gpt2

from transformers import pipeline

TOKEN = ''


en_to_fr = pipeline("translation_en_to_fr", model="Helsinki-NLP/opus-mt-en-fr")
fr_to_en = pipeline("translation_fr_to_en", model="Helsinki-NLP/opus-mt-fr-en")

bot = commands.Bot(command_prefix='?')


sess = gpt2.start_tf_sess()
gpt2.load_gpt2(sess, run_name='run1')


@bot.command(name='p')
async def prediction(ctx, *message: str):
    message = fr_to_en(' '.join(message))[0]['translation_text']
    text_generated = gpt2.generate(sess,
                                   length=250,
                                   temperature=0.7,
                                   prefix=message,
                                   nsamples=1,
                                   return_as_list=True
                                   )[0]
    for sentence in text_generated.split('.'):
        await ctx.send(en_to_fr(sentence)[0]['translation_text'])

print('Bot prêt')
bot.run(TOKEN)


