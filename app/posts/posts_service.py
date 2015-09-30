from google.appengine.ext import ndb
from ferris3 import Model, Service, hvild, auto_service
import ferris3 as f3


class Post(Model):
    title = ndb.StringProperty(indexed=True)
    content = ndb.TextProperty(indexed=True)


PostMessage = f3.model_message(Post)


@auto_service
class PostsService(Service):
    list = hvild.list(Post)
    get = hvild.get(Post)
    delete = hvild.delete(Post)
    insert = hvild.insert(Post)
    update = hvild.update(Post)
    paginated_list = hvild.paginated_list(Post, limit=3)

    @f3.auto_method(returns=PostMessage, name="get_by_title")
    def get_by_title(self, request, title=(str,)):
        query = Post.query(Post.title==title)
        post = query.get()
        if not post:
            raise f3.NotFoundException()
        if not post.key.kind() == 'Post':
            raise f3.InvalidRequestException()
        message = f3.messages.serialize(PostMessage, post)
        return message

