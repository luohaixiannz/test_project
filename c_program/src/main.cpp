#include <stdio.h>

#include "app.h"

int main(int argc, char** argv) {
    App& app = App::getInstance();
    
    if(!app.start()) {
        printf("app start fail\n");
    }
    
    app.shutdown();
    return 0;
}
