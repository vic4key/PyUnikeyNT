# PyUnikeyNT
Unikey NT with Python

## Chức năng
- [x] Lấy chế độ gõ hiện tại EN/VI
- [x] Chuyển chế độ gõ sang EN/VI
- [x] Hỗ trợ tất cả các phiên bản của Unikey NT

## Cài đặt
`pip install git+https://github.com/vic4key/PyUnikeyNT.git`

## Hướng dẫn
```python
class Mode(Enum):
  EN = 0 # Chế độ gõ tiếng anh
  VI = 1 # Chế độ gõ tiếng việt

def initialize(process_id=0) -> bool
def get_current_mode() -> Mode
def set_current_mode(mode: Mode)
```

## Sử dụng
<details>
<summary>Nhấn để xem ...</summary>

```python
# Chú ý:
# - Nhớ chạy chương trình Unikey NT trước khi chạy code.
# - Nếu Unikey NT chạy quyền Administrator thì code cũng cần quyền tương tự.
  
import PyUnikeyNT

succeed = PyUnikeyNT.initialize()
assert succeed, "initialize failed"

mode = PyUnikeyNT.get_current_mode()
print(mode)

mode = PyUnikeyNT.Mode(not mode.value)
PyUnikeyNT.set_current_mode(mode)

mode = PyUnikeyNT.get_current_mode()
print(mode)
```
</details>

## Minh họa
![](tests/test.png?)

## Biên dịch
<details>
<summary>Nhấn để xem ...</summary>

```
1. Cài đặt Vutils @ https://github.com/vic4key/Vutils.git
2. Lấy code @ git clone https://github.com/vic4key/PyUnikeyNT.git
3. Xong
```
</details>

## Contact
Feel free to contact via [Twitter](https://twitter.com/vic4key) / [Gmail](mailto:vic4key@gmail.com) / [Blog](https://blog.vic.onl/) / [Website](https://vic.onl/)
