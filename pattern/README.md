# ⭐ Terminal Star Animation

A simple Python program that creates a **moving star (`********`) animation** directly in the terminal.

The stars move from left to right and then back again, creating a smooth bouncing effect.

## 📸 Preview

```text
********
 ********
  ********
   ********
    ********
     ********
      ********
       ...
      ********
     ********
    ********
   ********
  ********
 ********
********
```

## 🚀 How It Works

The program continuously:

1. Prints `********` with a changing number of spaces before it.
2. Increases the number of spaces to move the stars to the right.
3. Once it reaches 20 spaces, it reverses direction.
4. Decreases the spaces to move the stars back to the left.
5. Repeats the animation until the user stops it.

## 🛠️ Requirements

* Python 3.x
* A terminal/command prompt

No external libraries are required.

## ▶️ Running the Program

Save the code as:

```text
zigzag.py
```

Then run:

```bash
python zigzag.py
```

On some systems, you may need:

```bash
python3 animation.py
```

## ⏹️ Stopping the Animation

Press:

```text
Ctrl + C
```

The program catches the `KeyboardInterrupt` and exits cleanly.


## ⚙️ Customization

### Change the animation speed

Modify:

```python
time.sleep(0.1)
```

For a faster animation:

```python
time.sleep(0.05)
```

For a slower animation:

```python
time.sleep(0.2)
```

### Change the star pattern

Replace:

```python
print('********')
```

with something like:

```python
print('★ ★ ★')
```

or:

```python
print('========>')
```

### Change the movement distance

Modify:

```python
if spaces == 20:
```

For example:

```python
if spaces == 40:
```

will make the animation travel farther across the terminal.

## 📄 License

This project is free to use, modify, and share.
