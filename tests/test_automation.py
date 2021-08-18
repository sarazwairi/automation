import pytest
from automation.automation import phone_num,email


def test_phone_num():
    actual=phone_num("001-415-879-4210Require building,4296619540Develop particular meeting side item ground onto. ")
    expected=['001-415-879-4210','429-661-9540']
    assert actual==expected

def test_email():
    actual=email("leeshelley@lowery.com Apply middle begin never computer")
    expected=["leeshelley@lowery.com"]
    assert actual==expected