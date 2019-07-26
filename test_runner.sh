for pack in `ls $PYTHONPATH/test/`;
    do
    echo "Tests run in $PYTHONPATH/test/$pack"
    pipenv run pytest -q test/${pack}/test_*.py;
    done
