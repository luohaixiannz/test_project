#include "app.h"
#include <stdio.h>
#include <unistd.h>
App& App::getInstance() {
       static App app;
       return app;
}

App::App() {
       m_stopped = false;
}
   
bool App::start() {
       printf("app startup\n");
       while (!m_stopped) {
            printf("app run\n");
            sleep(5);
       }
       return true;
}

   bool App::shutdown() {
       if (m_stopped == false) {
           m_stopped = true; 
       }
       return true;
}
