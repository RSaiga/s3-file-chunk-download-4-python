import boto3

class FileRepositoryOnS3:
  def __init__(self):
    self._s3 = boto3.client('s3')

  def find(self, bucket, key):
    response = self._s3.get_object(Bucket=bucket, Key=key)
    body = response['Body']
    return body

def download():
  chunk_size = 1000000
  newline = '\n'.encode()
  partial_chunk = b''

  repository = FileRepositoryOnS3()
  body = repository.find('YOUR BUCKET NAME', 'YOUR KEY')

  while (True):
    chunk = partial_chunk + body.read(chunk_size)
    last_newline = chunk.rfind(newline)
    lines = chunk[0:last_newline+1].decode('utf-8').split('\r\n')

    print(lines)

    partial_chunk = chunk[last_newline+1:]

if __name__ == '__main__':
  download()