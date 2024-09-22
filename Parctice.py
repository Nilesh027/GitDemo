

def greet(fx):
  def mfx(*args, **kwargs):
    print("Good Morning")
    fx(*args, **kwargs)
    print("Thanks for using this function")
  return mfx
  
@greet


def hello():
  print("Hello World")

@greet
def add(a,b):
  print(a + b)
 
# greet(hello)() same work as @greet
hello()
add(2,3)