
package com.epam.java.util;

import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

public class Logging {
    
    private static final Logger logger = LogManager.getLogger();
    private static final String PREFIX = " >> ";
    
    private Logging() {}
    
    public static Logger getLogger() {
        return logger;
    }
    
    public static class Logger {
        
        private final org.apache.logging.log4j.Logger logger;
        
        public Logger() {
            logger = LogManager.getLogger();
        }
        
        public void info(String message) {
            logger.info(PREFIX + message);
        }
        
        public void error(Throwable e) {
            logger.error(e);
        }
    }
    
}
