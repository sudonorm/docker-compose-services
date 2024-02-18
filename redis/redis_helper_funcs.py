import redis

r = redis.Redis(host='localhost', port=6379, db=0, encoding='utf-8', decode_responses=True)

def enqueue_value(*, queue_name:str, queue_value:str):
    """Create a set queue

    Args:
        queue_name (str): name of the key to use for the queue
        queue_value (str): value of the key

    """
    return r.sadd(queue_name, queue_value)

def dequeue_value(*, queue_name:str,):
    """Pop from a set queue

    Args:
        queue_name (str): name of the key in the queue

    """
    return r.spop(queue_name)

def get_all_keys_in_redis_store() -> list:
    """Get a list of all keys in a redis store

    Returns:
        list: keys in the redis store
    """
    return sorted([x for x in r.scan_iter('*')])

def get_members(*, queue_name:str,) -> list:
    """Return the members of a set queue

    Args:
        queue_name (str): name of the key in the queue

    Returns:
        tuple: Union[list, int]: list of members, count of members
    """
    members = list(r.smembers(queue_name))

    return (members, len(members))
