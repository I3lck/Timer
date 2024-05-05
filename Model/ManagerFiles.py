import os


class ManagerFiles:
    # $! Доработать функционал

    sufVfs = '.svg'
    sufCnf = '.xml'

    def getPathsFiles(self, pathDir):
        return [r + '\\' + f for r, _, fs in os.walk(pathDir) for f in fs]

    def getPathsFilesWithSuf(self, pathDir, sufFiles):
        return [r + '\\' + f for r, _, fs in os.walk(pathDir) for f in fs if f.endswith(sufFiles)]

    def getPathsVfs(self, pathDir):
        return self.getPathsFilesWithSuf(pathDir, self.sufVfs)

    def getNamesVfs(self, pathDir):
        """Получить имена ВК без суффиксов"""
        return [self.getNameVf(f) for _, _, fs in os.walk(pathDir) for f in fs if f.endswith(self.sufVfs)]

    def getPathsCnfs(self, pathDir):
        return self.getPathsFilesWithSuf(pathDir, self.sufCnf)

    def getPathsFilesWithoutSuf(self, pathDir, sufFiles):
        return [r + '\\' + f for r, _, fs in os.walk(pathDir) for f in fs if not f.endswith(sufFiles)]

    @classmethod
    def getNameVf(cls, pathVf):
        return pathVf.split('\\')[-1][:-4]


if __name__ == '__main__':
    pass
