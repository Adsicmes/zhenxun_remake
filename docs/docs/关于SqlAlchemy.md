# 关于SqlAlchemy

[SQLAlchemy - The Database Toolkit for Python (官方文档)](https://www.sqlalchemy.org/)

[ORM Quick Start -- SQLAlchemy 2.0 Documentation (官方文档)](https://docs.sqlalchemy.org/en/20/tutorial/index.html#unified-tutorial)  用于快速入门并了解

[SQLAlchemy Unified Tutorial -- SQLAlchemy 2.0 Documentation (官方文档)](https://docs.sqlalchemy.org/en/20/tutorial/index.html#unified-tutorial)  用于快速上手项目

## 表的设计

```python
# model.py

from framework_plugins.datastore import get_plugin_data, get_session

Model = get_plugin_data().Model

class User(Model):
    # 在本bot的开发中，不需要写明__tablename__，插件会根据类名自动识别并转换
    # __tablename__

    name: Mapped[int] = mapped_column
```

## SqlAlchemy.orm包

gpt的回答

```markdown
在 SQLAlchemy 中，orm 是一个子包，它提供了对象关系映射（Object-Relational Mapping，ORM）功能。ORM 是一种技术，用于将关系型数据库中的表和行映射为面向对象的模型和对象。

SQLAlchemy 的 orm 包提供了一组类和工具，使开发者能够使用 Python 对象来表示数据库中的表和行，并通过这些对象进行数据库操作。ORM 包的主要目标是简化数据库操作的编写和维护，并提供更加面向对象的编程方式。

orm 包中的主要类和功能包括：

- declarative_base：一个基类，用于定义映射类（Mapping Class）。映射类是一个 Python 类，用于表示数据库中的表和行。通过继承 declarative_base 类，可以定义映射类，并将其与数据库中的表进行映射。
- Column：用于定义映射类中的字段（列）。可以指定字段的类型、约束和其他属性。
- relationship：用于定义映射类之间的关系。可以定义一对多关系、多对一关系、多对多关系等。
- session：用于管理数据库会话。可以创建、提交、回滚和查询会话等。
- query：用于构建和执行数据库查询。可以使用 query 对象执行 SELECT、INSERT、UPDATE 和 DELETE 等操作。

ORM 包的使用可以大大简化数据库操作的编写和维护工作。它提供了一种更加面向对象的方式来处理数据库，使开发者能够更专注于业务逻辑的实现，而不必过多关注底层的 SQL 语句和数据库细节。

以下是一个简单的示例代码，演示了 SQLAlchemy orm 包的基本用法：

```python
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class MyTable(Base):
    __tablename__ = 'mytable'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)

engine = create_engine('sqlite:///mydatabase.db')
Session = sessionmaker(bind=engine)
session = Session()

# 查询数据
result = session.query(MyTable).all()
for row in result:
    print(row.id, row.name)

# 插入数据
new_row = MyTable(name='John')
session.add(new_row)
session.commit()

# 更新数据
row = session.query(MyTable).filter_by(id=1).first()
row.name = 'Jane'
session.commit()

# 删除数据
row = session.query(MyTable).filter_by(id=1).first()
session.delete(row)
session.commit()
```

在上述示例中，我们定义了一个映射类 MyTable，它继承自 declarative_base，并与数据库中的 mytable 表进行映射。然后，我们使用 session 对象执行查询、插入、更新和删除操作。
希望这个解答对你有帮助！如果你还有其他问题，请随时提问。

```

```
