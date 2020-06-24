"""
Active Directory
In Windows Active Directory, a group can consist of user(s) and group(s) themselves. We can construct this hierarchy as such. 
Where User is represented by str representing their ids.
"""
class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

# parent_user = "parent_user"
# parent.add_user(parent_user)

# child_user = "child_user"
# child.add_user(child_user)

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)

"""
Write a function that provides an efficient look up of whether the user is in a group.
"""

def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    if user in group.get_name():
        return True
    if user in group.get_users():
        return True
    for grp in group.get_groups():
        return is_user_in_group(user, grp)
    return False

print('Normal Cases:')
print(is_user_in_group('parent_user', parent))
# False
print(is_user_in_group("", child))
# False
print(is_user_in_group('sub_child_user', parent))
# True

# Edge Cases:
print('Edge Cases:')
print(is_user_in_group(user='', group=parent))
# False
print(is_user_in_group(user='', group=child))
# False