import pymysql

conn = pymysql.connect(host="localhost" , user="root" , password="" , database="cms")


def delete(table,primary_id,id):
    with conn.cursor() as cur:
        sql=f"delete from {table} where {primary_id}={id}"
        status=cur.execute(sql)
        conn.commit()

    if status:
        return True
    else:
        return False