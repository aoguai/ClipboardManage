# ClipboardManage

ClipboardManage 是一个用于操作 Windows 剪贴板的 Python 轻量工具类。

ClipboardManage is a lightweight Python utility class for manipulating the Windows clipboard.

## 导言

ClipboardManage 有一些优点和功能上的差异：

1. **功能丰富**：ClipboardManage 提供了更多功能，可以操作剪贴板中的文件路径、图像数据和文本。它支持设置和读取文件路径列表、图像数据和文本，以及判断文件是否为图像等功能。

2. **支持文件路径列表**：ClipboardManage 允许将多个文件路径设置到剪贴板中，并可以读取剪贴板中的文件路径列表。这对于处理多个文件路径的场景非常有用。

3. **图像操作**：ClipboardManage 提供了复制图像到剪贴板的方法，可以将指定路径的图像复制到剪贴板中。这在需要处理图像数据的场景下很有用。

4. **更灵活的文本操作**：ClipboardManage 允许设置多个文本并使用自定义的连接符将它们连接起来。这对于需要处理多个文本片段的场景非常有用。

总体而言，ClipboardManage 在功能和灵活性方面相对更好，特别适用于需要处理文件路径、图像和文本的剪贴板操作场景。

如果你的需求主要集中在文本的复制和粘贴操作上，或者有跨系统需求，那么 `pyperclip` 和 `clipboard` 这样的库可能更适合你的需求。

## 安装

请按照以下步骤进行安装：

1. 确保已安装 Python（建议使用 Python 3.x 版本）。
2. 在命令行中使用以下命令安装所需的依赖项：

```
pip install -r requirement.txt
```

## 使用方法

ClipboardManage 提供了以下主要功能：

### 设置剪贴板内容

要将文件绝对路径、图像数据或文本设置到剪贴板中，请使用以下方法：

#### 设置文件绝对路径到剪贴板

```python
ClipboardManager.set_clipboard(file_paths)
```

其中 `file_paths` 是要设置到剪贴板的文件绝对路径的列表。

#### 设置图像数据到剪贴板

```python
ClipboardManager.set_clipboard([image_path], is_text=False)
```

其中 `image_path` 是要设置到剪贴板的图像文件的绝对路径。

#### 设置文本到剪贴板

```python
ClipboardManager.set_clipboard([text], is_text=True)
```

其中 `text` 是要设置到剪贴板的文本。

### 读取剪贴板内容

要从剪贴板中读取文件路径、图像数据或文本，请使用以下方法：

#### 读取剪贴板中的文件路径

```python
file_paths = ClipboardManager.readClipboardFilePaths()
```

返回值 `file_paths` 是剪贴板中的文件绝对路径列表。

#### 读取剪贴板中的图像数据

```python
image_data = ClipboardManager.readClipboardIMGPaths()
```

返回值 `image_data` 是剪贴板中的图像数据。

#### 读取剪贴板中的文本

```python
text = ClipboardManager.readClipboardText()
```

返回值 `text` 是剪贴板中的文本。

### 示例代码

以下是一些使用 ClipboardManage 完成常见的剪贴板操作的示例代码：

#### 设置文件路径到剪贴板并读取

```python
file_paths = ["C:/path/to/file1.txt", "C:/path/to/file2.txt"]
ClipboardManager.set_clipboard(file_paths)
read_file_paths = ClipboardManager.readClipboardFilePaths()
print(read_file_paths)
```

#### 设置图像数据到剪贴板并读取

```python
image_path = "C:/path/to/image.png"
ClipboardManager.set_clipboard([image_path], is_text=False)
image_data = ClipboardManager.readClipboardIMGPaths()
print(image_data)
```

#### 设置文本到剪贴板并读取

```python
text = "Hello, ClipboardManage!"
ClipboardManager.set_clipboard([text], is_text=True)
read_text = ClipboardManager.readClipboardText()
print(read_text)
```

## 授权许可

此存储库遵循 MIT 开源协议，请务必理解。

我们严禁所有通过本程序违反任何国家法律的行为，请在法律范围内使用本程序。

默认情况下，使用此项目将被视为您同意我们的规则。请务必遵守道德和法律标准。

如果您不遵守，您将对后果负责，作者将不承担任何责任！
