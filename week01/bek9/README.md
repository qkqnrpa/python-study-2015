# Python3 Install

## Python3 install using brew

brew로 python3를 설치해 보기로 했다.

```
$ brew install python3
```

bash 권한 문제 때문인지 설치가 제대로 안 됐다. 설치 완료 후 마지막에 아래와 같은 메시지를 뿜었다:

```
Error: An unexpected error occurred during the `brew link` step
The formula built, but is not symlinked into /usr/local
Permission denied - /usr/local/Frameworks
Error: Permission denied - /usr/local/Frameworks
GimHyeonjongs-MacBook-Pro:~ bek9$ aq    \
```

brew doctor 해 보니 다음과 같았다:

```
$ brew doctor
Please note that these warnings are just used to help the Homebrew maintainers
with debugging if you file an issue. If everything you use Homebrew for is
working fine: please don't worry and just ignore them. Thanks!

Warning: The /usr/local is not writable.
You should probably `chown` /usr/local

Warning: The /usr/local directory is not writable.
Even if this directory was writable when you installed Homebrew, other
software may change permissions on this directory. Some versions of the
"InstantOn" component of Airfoil are known to do this.

You should probably change the ownership and permissions of /usr/local
back to your user account.
  sudo chown -R $(whoami):admin /usr/local

Warning: You have unlinked kegs in your Cellar
Leaving kegs unlinked can lead to build-trouble and cause brews that depend on
those kegs to fail to run properly once built. Run `brew link` on these:
    python3
```

우선 chown으로 /usr/local 권한을 줬다.

```
$ sudo chown -R $USER /usr/local
```

다시 doctor하니 링크만 남았다.

```
$ brew doctor
Please note that these warnings are just used to help the Homebrew maintainers
with debugging if you file an issue. If everything you use Homebrew for is
working fine: please don't worry and just ignore them. Thanks!

Warning: You have unlinked kegs in your Cellar
Leaving kegs unlinked can lead to build-trouble and cause brews that depend on
those kegs to fail to run properly once built. Run `brew link` on these:
    python3
```

그냥 링크하니 깔끔하게 끝났다.

```
$ brew link python3
Linking /usr/local/Cellar/python3/3.4.3_2... 19 symlinks created
$ brew doctor
Your system is ready to brew.
```

## Python Version Check

버전 확인 옵션은 `-V`다. **대문자**다. 또는 `--version`

```
$ python -V
Python 2.7.10
$ python --version
Python 2.7.10
```

## Python Exit

python 명령어로 파이썬 CLI로 진입했을 때 `exit` 명령어나 `Ctrl+C`가 아닌 `exit()` 함수 호출이나 `Ctrl+D`로 빠져나와야 한다.

```
$ python
Python 2.7.10 (default, Aug 22 2015, 20:33:39) 
[GCC 4.2.1 Compatible Apple LLVM 7.0.0 (clang-700.0.59.1)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> exit
Use exit() or Ctrl-D (i.e. EOF) to exit
>>> exit()
```

## Execute Python3

python3 설치 후 환경변수 등을 변경해야 하는 줄 알았는데 python3는 아예 명령어가 달랐다. 허무 :/

```
$ python3
Python 3.4.3 (default, Oct  6 2015, 23:23:31) 
[GCC 4.2.1 Compatible Apple LLVM 7.0.0 (clang-700.0.72)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> exit()
$ python3 -V
Python 3.4.3
```