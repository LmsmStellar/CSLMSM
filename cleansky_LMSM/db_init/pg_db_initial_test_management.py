import pg_db_initial_root_account
import pg_db_initial_version_1
import pg_db_initial

# try:
#     sql = """
#     INSERT INTO account(orga, uname, password)
#     VALUES ('orga1', 'tu1', '12345678');
#     """
#     pg_db_initial.cur.execute(sql)
#     pg_db_initial.conn.commit()
#
#     sql = """
#     INSERT INTO account(orga, uname, password)
#     VALUES ('orga1', 'tu2', '12345678');
#     """
#     pg_db_initial.cur.execute(sql)
#     pg_db_initial.conn.commit()
#
# except:
#     print("fail")

try:
    sql = """
        INSERT INTO account(orga, uname, password)
        VALUES ('orga_1', 'admini_1', '0000');
        """
    pg_db_initial.cur.execute(sql)
    pg_db_initial.conn.commit()

    sql = """
        INSERT INTO user_right(id_account, role, id_test_mean)
        VALUES (3, 2, 1);
        """
    pg_db_initial.cur.execute(sql)
    pg_db_initial.conn.commit()

    sql = """
            INSERT INTO account(orga, uname, password)
            VALUES ('orga_1', 'admini_2', '0000');
            """
    pg_db_initial.cur.execute(sql)
    pg_db_initial.conn.commit()

    sql = """
        INSERT INTO user_right(id_account, role, insect)
        VALUES (3, 4, true);
        INSERT INTO user_right(id_account, role, insect)
        values (4, 5, false);
        INSERT INTO user_right(id_account, role, acqui_system)
        values (3, 5, false);
        INSERT INTO user_right(id_account, role, id_test_mean)
        values (3, 2, 1);
        INSERT INTO user_right(id_account, role, id_test_mean)
        values (4, 2, 2);
        INSERT INTO user_right(id_account, role, id_type_coating)
        values (3, 3, 1);
        INSERT INTO user_right(id_account, role, id_type_coating)
        values (4, 3, 2);
        """
    pg_db_initial.cur.execute(sql)
    pg_db_initial.conn.commit()

    print("test_management initial success")
except:
    print("test_management initial fail")
