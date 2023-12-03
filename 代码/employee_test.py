import pytest

from employee import Employee


@pytest.fixture
def example_employee():
    example_employee = Employee("小明", "张", 150000)
    return example_employee


# 测试默认工资涨幅情况
def test_give_default_raise(example_employee):
    example_employee.give_raise()
    assert example_employee.salary == 155000


# 测试自定义工资涨幅情况
def test_give_custom_raise(example_employee):
    example_employee.give_raise(10000)
    assert example_employee.salary == 160000
