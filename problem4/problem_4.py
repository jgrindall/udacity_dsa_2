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
    
    def __repr__(self):
        users = str(self.users)
        group_names = [group.name for group in self.groups]
        return "Group:{0} u:{1} g:{2}".format(self.name, users, group_names)
     
    def __str__(self):
         return self.__repr__()
     
    @staticmethod
    def is_user_in_group(user, group):
        """
        Return True if user is in the group, False otherwise.
    
        Args:
          user(str): user name/id
          group(class:Group): group to check user membership against
        """
        
        checked_groups = {}
        
        def _is_user_in_group(user, group):
            
            nonlocal checked_groups
            
            # we already checked this group - note that Active Directory structures can be circular
            if group in checked_groups:
                return False
            else:
                if user in group.get_users():
                    return True
                else:
                    checked_groups[group] = "in_progress"
                    for group in group.get_groups():
                        if _is_user_in_group(user, group):
                            return True
                    checked_groups[group] = "done"
            return False
    
        return _is_user_in_group(user, group)


