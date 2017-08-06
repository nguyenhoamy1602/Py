from eventregistry import *
er = EventRegistry(apiKey = "0a89c702-b49e-4b8f-a3c1-6280be5dcb11")
q = QueryArticlesIter(conceptUri = er.getConceptUri("George Clooney"), lang = "eng")
for art in q.execQuery(er, sortBy = "rel", maxItems=3):
    print art