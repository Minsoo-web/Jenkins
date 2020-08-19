# PARAMS-E2E

## parameter

### build_target = IRIS-E2E

    user : root / user0
    menu_target : 00.SETUP / 01.ANALYZER / ...

### build_target = IRIS-E2E-SAAS

    user : admin / NO_USER / REGULAR_USER
    menu_target : {
        admin : ['01.USER','02.BLOG','03.PRODUCT']
        NO_USER && REGULAR_USER : ['00.MAIN','01.PRODUCT'...]
    }
