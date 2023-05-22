from ctypes import Structure, c_uint, c_long, c_int, c_bool, sizeof, c_char, memmove, addressof, c_wchar
from typing import List
import win32clipboard
from PIL import Image, UnidentifiedImageError
from io import BytesIO


class ClipboardManager:
    """
    ClipboardManager是一个用于操作剪贴板的工具类。

    它提供了一些方法用于设置、读取和操作剪贴板中的文件绝对路径、图像数据和文本。
    """

    class DROPFILES(Structure):
        """
        DROP FILES结构体表示在剪贴板中放置文件列表的数据结构。
        """
        _fields_ = [
            ("pFiles", c_uint),
            ("x", c_long),
            ("y", c_long),
            ("fNC", c_int),
            ("fWide", c_bool),
        ]

    def __init__(self):
        """
        创建一个ClipboardManager对象。
        """
        pass

    @staticmethod
    def setClipboardFiles(paths):
        """
        将文件绝对路径列表设置到剪贴板中。

        :param paths: 要设置到剪贴板的文件绝对路径的列表。
        :type paths: list[str]

        """
        pDropFiles = ClipboardManager.DROPFILES()
        total_length = sum(len(path) + 1 for path in paths) + 1
        pDropFiles.pFiles = sizeof(ClipboardManager.DROPFILES)
        pDropFiles.x = 0
        pDropFiles.y = 0
        pDropFiles.fNC = 0
        pDropFiles.fWide = True
        buffer_length = sizeof(pDropFiles) + total_length * sizeof(c_wchar)
        buffer = (c_char * buffer_length)()
        memmove(buffer, addressof(pDropFiles), sizeof(pDropFiles))
        offset = sizeof(pDropFiles)
        for path in paths:
            wide_path = path.replace("/", "\\").encode("utf-16le")
            memmove(addressof(buffer) + offset, wide_path, len(wide_path) + 1)
            offset += len(wide_path) + sizeof(c_wchar)
        buffer[offset] = b'\0'
        win32clipboard.OpenClipboard()
        try:
            win32clipboard.EmptyClipboard()
            win32clipboard.SetClipboardData(win32clipboard.CF_HDROP, buffer)
        finally:
            win32clipboard.CloseClipboard()

    @staticmethod
    def readClipboardFilePaths() -> List[str]:
        """
        从剪贴板中读取文件绝对路径列表。

        :return: 剪贴板中的文件绝对路径列表。
        :rtype: list[str]

        """
        win32clipboard.OpenClipboard()
        try:
            return win32clipboard.GetClipboardData(win32clipboard.CF_HDROP)
        finally:
            win32clipboard.CloseClipboard()

    @staticmethod
    def readClipboardIMGPaths() -> bytes:
        """
        从剪贴板中读取图像数据。

        :return: 剪贴板中的图像数据。
        :rtype: bytes

        """
        win32clipboard.OpenClipboard()
        try:
            return win32clipboard.GetClipboardData(win32clipboard.CF_DIB)
        finally:
            win32clipboard.CloseClipboard()

    @staticmethod
    def readClipboardText() -> str:
        """
        从剪贴板中读取文本。

        :return: 剪贴板中的文本。
        :rtype: str

        """
        win32clipboard.OpenClipboard()
        try:
            return win32clipboard.GetClipboardData(win32clipboard.CF_UNICODETEXT)
        finally:
            win32clipboard.CloseClipboard()

    @staticmethod
    def copy_image_to_clipboard(img_path: str):
        """
        将指定绝对路径的图像复制到剪贴板中。

        :param img_path: 要复制的图像的绝对路径。
        :type img_path: str

        """
        image = Image.open(img_path)
        output = BytesIO()
        image.save(output, 'BMP')
        data = output.getvalue()[14:]
        output.close()
        win32clipboard.OpenClipboard()
        try:
            win32clipboard.EmptyClipboard()
            win32clipboard.SetClipboardData(win32clipboard.CF_DIB, data)
        finally:
            win32clipboard.CloseClipboard()

    @staticmethod
    def copy_text_to_clipboard(text: str):
        """
        将指定的文本复制到剪贴板中。

        :param text: 要复制的文本。
        :type text: str

        """
        win32clipboard.OpenClipboard()
        try:
            win32clipboard.EmptyClipboard()
            win32clipboard.SetClipboardData(win32clipboard.CF_UNICODETEXT, text)
        finally:
            win32clipboard.CloseClipboard()

    @staticmethod
    def is_image(filename) -> bool:
        """
        判断给定的文件是否为图像文件。

        :param filename: 要检查的文件的绝对路径。
        :type filename: str
        :return: 如果文件是图像文件，则为True，否则为False。
        :rtype: bool

        """
        try:
            with Image.open(filename):
                return True
        except UnidentifiedImageError:
            return False

    @staticmethod
    def set_clipboard(file_paths, is_text=False, delimiter='\n') -> List[str] or bytes or str:
        """
        将指定的文件绝对路径、图像或文本复制到剪贴板中。

        :param file_paths: 要复制到剪贴板的文件绝对路径或文本的列表。
        :type file_paths: list[str]
        :param is_text: 指示是否为文本类型。
        :type is_text: bool
        :param delimiter: 连接多个文本之间的连接符号。
        :type delimiter: str
        :return: 剪贴板中的文件绝对路径列表、图像数据或文本。
        :rtype: list[str] or bytes or str

        """

        if not file_paths:
            return []

        if is_text:
            text = delimiter.join(file_paths)
            ClipboardManager.copy_text_to_clipboard(text)
            return ClipboardManager.readClipboardText()
        elif len(file_paths) == 1 and ClipboardManager.is_image(file_paths[0]):
            ClipboardManager.copy_image_to_clipboard(file_paths[0])
            return ClipboardManager.readClipboardIMGPaths()
        else:
            ClipboardManager.setClipboardFiles(file_paths)
            return ClipboardManager.readClipboardFilePaths()


text = "Hello, ClipboardManage!"
ClipboardManager.set_clipboard([text], is_text=True)
read_text = ClipboardManager.readClipboardText()
print(read_text)
