def build_profile(first, last, **user_info):
    """Buat dictionary berisi semua yang kita ketahui tentang seorang pengguna."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


user_profile = build_profile(
    'Nathaniela', 'Berliana',
    university='Universitas Sebelas Maret',
    major='Teknik Industri',
    location='Surakarta',
)

for key, value in user_profile.items():
    print(f"{key}: {value}")