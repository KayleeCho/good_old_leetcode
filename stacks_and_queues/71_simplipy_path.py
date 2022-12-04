class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """

        stack = []

        for token in path.split('/'):
            if token == '.' or not token:
                continue
            elif token == '..':
                if stack: stack.pop()
            else:
                stack.append(token)

        return "/" + "/".join(stack)
