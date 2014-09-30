from __future__ import unicode_literals

# flipping words, simple example
print('\n~~ simple flipping example ~~\n')
doc = 'The pro-democracy demonstrations in Hong Kong, which expanded into additional neighborhoods on Tuesday in defiance of new government warnings, have been a diligently clean, exceedingly polite and scrupulously peaceful insurgency that supporters have taken to calling the Umbrella Revolution.'

new_doc = doc.replace('Hong Kong', 'Ferguson')
print(new_doc)


# a more complex example
print('\n~~ more complex flipping example ~~\n')
doc = 'China\'s state-run news outlets have depicted the protests as the handiwork of a conspiracy aided by the West to topple the Communist Party. But what leaders in Beijing and Hong Kong face is something even more alien to party thinking: an amorphous movement that does not answer to any particular individual or agenda.'

new_doc = doc.replace('China', 'America').replace('West', 'East').replace('Communist', 'Democratic').replace('Beijing', 'Washington').replace('Hong Kong', 'Ferguson')
print(new_doc)


# but that's kind of ugly so...
from flipper import flip_words

print('\n~~ cleaner flipping ~~\n')
mappings = {
    'China': 'America',
    'West': 'East',
    'Communist': 'Democratic',
    'Beijing': 'Washington',
    'Hong Kong': 'Ferguson'
}
new_doc = flip_words(doc, mappings)
print(new_doc)


# example using a class!!
from flipper import Flipper
print('\n~~ flipping with a class ~~\n')
f = Flipper(mappings)
new_doc = f.flip(doc)
print(new_doc)


# let's do it straight from urls
# pip install requests
# pip install readability-lxml
import requests
from readability.readability import Document

print('\n~~ flipping from urls ~~\n')

urls = [
    'http://www.nytimes.com/2014/10/01/world/asia/in-hong-kong-clean-and-polite-but-a-protest-nonetheless.html',
    'http://www.nytimes.com/2014/10/01/world/asia/hong-kong-protests.html'
]

for url in urls:
    response = requests.get(url)

    doc = Document(response.content).summary()
    new_doc = flip_words(doc, mappings)
    #new_doc = flip_words(response.content.decode('utf-8'), mappings)

    # splice in encoding info so it renders properly in the browser
    if '<head>' in new_doc:
        new_doc = new_doc.replace('<head>', '<head><meta charset="utf-8">')
    else:
        new_doc = new_doc.replace('<body>', '<head><meta charset="utf-8"></head><body>')

    filename = url.split('/')[-1]
    print('saving output to file called {0}'.format(filename))
    with open(filename, 'wb') as output:
        output.write(new_doc.encode('utf-8'))
