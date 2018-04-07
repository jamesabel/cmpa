
import os
import stat
import shutil
import logging
import time

log = logging.getLogger()


def remove_readonly(path):
    os.chmod(path, stat.S_IWRITE)


# sometimes needed for Windows
def _remove_readonly_onerror(func, path, excinfo):
    os.chmod(path, stat.S_IWRITE)
    func(path)


def rmdir(p):
    retry_count = 10
    delete_ok = False
    while os.path.exists(p) and retry_count > 0:
        try:
            shutil.rmtree(p, onerror=_remove_readonly_onerror)
            delete_ok = True
        except FileNotFoundError as e:
            log.debug(str(e))  # this can happen when first doing the shutil.rmtree()
            time.sleep(1)
        except PermissionError as e:
            log.info(str(e))
            time.sleep(1)
        retry_count -= 1
    if os.path.exists(p):
        log.error('could not remove "%s"' % p)
    return delete_ok and retry_count > 0


def mkdirs(d):
    # sometimes when os.makedirs exits the dir is not actually there
    while not os.path.exists(d):
        os.makedirs(d, exist_ok=True)
