import os

class FileUtils:
    
    @staticmethod
    def find_files(suffix, path):
        paths = []
        
        def _find_files(path):
            if not os.path.exists(path):
                return
            entries = os.listdir(path)
            for entry in entries:
                full_path = os.path.join(path, entry)
                if os.path.isfile(full_path) and entry.endswith(suffix):
                    paths.append(full_path)
                elif os.path.isdir(full_path):
                    _find_files(full_path)
    
        _find_files(path)
        return paths

