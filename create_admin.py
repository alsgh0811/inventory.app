from app import app, db, User, Branch
from werkzeug.security import generate_password_hash

with app.app_context():

    # 1사업소 생성
    branch = Branch(name="영흥사업소")
    db.session.add(branch)
    db.session.commit()

    # 관리자 생성
    admin = User(
        username="admin",
        password=generate_password_hash("admin1234"),
        role="admin",
        is_active=True,
        is_superadmin=True,
        branch_id=branch.id
    )

    db.session.add(admin)
    db.session.commit()

    print("초기 관리자 및 사업소 생성 완료")
