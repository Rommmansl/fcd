from django.db import models
from django.core.files.storage import FileSystemStorage
from PIL import Image

_MAX_SIZE = 300
class OverwriteStorage(FileSystemStorage):
  def _save(self, name, content):
    if self.exists(name):
      self.delete(name)
    return super(OverwriteStorage, self)._save(name, content)

  def get_available_name(self, name, max_length=None):
    return name

def image_folder(instance, filename1):
  filename1 = '1' + '.' + 'jpg'
  return "{0}/{1}".format('static/vid4/image', filename1)

class Picture(models.Model):

  picfile = models.ImageField(upload_to=image_folder,
        storage=OverwriteStorage())

  def save(self, *args, **kwargs):
    # Сначала - обычное сохранение
    super(Picture, self).save(*args, **kwargs)

    # Проверяем, указан ли логотип
    if self.picfile:
      filepath = self.picfile.path
      width = self.picfile.width
      height = self.picfile.height

      max_size = max(width, height)

      # Может, и не надо ничего менять?
      if max_size > _MAX_SIZE:
        # Надо, Федя, надо
        image = Image.open(filepath)
        # resize - безопасная функция, она создаёт новый объект, а не
        # вносит изменения в исходный, поэтому так
        image = image.resize(
          (round(width / max_size * _MAX_SIZE),  # Сохраняем пропорции
           round(height / max_size * _MAX_SIZE)),
          Image.ANTIALIAS
        )
        # И не забыть сохраниться
        image.save(filepath)

