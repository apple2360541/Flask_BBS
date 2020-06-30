## 分组：
权限有很多，一个模型就有最少三个权限，如果一些用户拥有相同的权限，那么每次都要重复添加。这时候分组就可以帮我们解决这种问题了，我们可以把一些权限归类，然后添加到某个分组中，之后再把和把需要赋予这些权限的用户添加到这个分组中，就比较好管理了。分组我们使用的是`django.contrib.auth.models.Group`模型， 每个用户组拥有`id`和`name`两个字段，该模型在数据库被映射为`auth_group`数据表。

### 分组操作：

1. `Group.object.create(group_name)`：创建分组。
2. `group.permissions`：某个分组上的权限。多对多的关系。
    * `group.permissions.add`：添加权限。
    * `group.permissions.remove`：移除权限。
    * `group.permissions.clear`：清除所有权限。

3. `user.groups`：某个用户上的所有分组。多对多的关系。