from django.core.cache import cache
from chunks import CACHE_PREFIX 

def chunk_post_save(sender, **kwargs):

    instance = kwargs.get('instance')
    if instance:
        cache_key = "%s%s" % (CACHE_PREFIX, instance.key )
        cache.delete(cache_key)
