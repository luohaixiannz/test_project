#ifndef APP_H
#define APP_H 

class App{
    public:
        static App& getInstance();
        bool start();
        bool shutdown();
        
    private:
        App();
        App(const App&);
        App& operator=(const App&);
        bool m_stopped;
};

#endif
