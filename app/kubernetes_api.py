from flask_caching import Cache

cache = Cache(config={'CACHE_TYPE': 'simple'})

def init_app(app):
    cache.init_app(app)

@cache.cached(timeout=300)  # Cache the result for 5 minutes (300 seconds)
def get_cluster_info():
    return {
        'cluster_name': 'example-cluster',
        'nodes': 3,
        'namespaces': 2
}
