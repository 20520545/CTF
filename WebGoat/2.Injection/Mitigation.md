
## Mitigation
### Contruction for defense against SqlInjectionAdvanced

5. Try it! Writing safe code

Connection conn= DriverManager.`getConnection`(_);
`PreparedStatement ps`= conn.`prepareStatement`("SELECT status FROM users WHERE name=`?` AND mail= `?`");
`ps.setString(1, "users")`;
`ps.setString(2, "mail")`;


6. Try it! Writing safe code

```
try {  
     Connection conn = DriverManager.getConnection(DBURL, DBUSER, DBPW);  
     PreparedStatement ps = conn.prepareStatement("SELECT * FROM users WHERE name = ?");  
     ps.setString(1, "admin");  
     ps.executeUpdate();  
} catch (Exception e) {  
     System.out.println("Drop!");  
}
```

9. Input validation alone is not enough!!!

Bypass whitespace filter by comment /**/ and using 'null' to brute column of the database because if you only use the previous name of the database, it won't allow because of missing column names.
```
'/**/union/**/select/**/userid,user_name,password,cookie,null,null,null/**/from/**/user_system_data--
```

refs: https://portswigger.net/support/sql-injection-bypassing-common-filters

10. Input validation alone is not enough!!!
Filter improve blacklists.
```
'union/**/selselectect/**/userid,user_name,password,cookie,null,null,null/**/frfromom/**/user_system_data--
```
 
12. List of servers

Brute force by running from 0.130.219.202 to 255.130.219.202 to get the answer.

Ip: 104.130.219.202