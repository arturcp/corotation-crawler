#!/usr/bin/python
class Cluster():
    # Byte-by-byte Description of file:  clustersGAL.txt
    # https://wilton.unifei.edu.br/ocdb/readme.txt
    # -------------------------------------------------------------------------------------------------
    #    Bytes Format Units   Label     Explanations
    # -------------------------------------------------------------------------------------------------
    #    1- 18  A18   ---     Name      Cluster name
    #   19- 26  F8.4  deg     GLON      Galactic longitude II (J2000.0)
    #       33  A1    ---     DE-       Galactic latitude sign (J2000.0)
    #   34- 40  F7.4  deg     GLAT      Galactic latitude II (J2000.0)
    #   47- 48  A2    ---     class     [*] Flag for classification of the cluster
    #   54- 58  F5.1  arcmin  Diam      Apparent diameter in arcmin
    #   62- 66  I5    pc      d         Distance
    #   72- 76  F5.3          EBV       Colour excess in BV
    #   80- 85  F6.3  yr      Age       Age (in log t)
    #       91  A1    ---     pml- 	  Mean proper motion of the cluster mu_l sign
    #   92- 96  F5.2  mas/yr  pml       Mean proper motion of the cluster in mul, ICRS
    #   99-102  F3.2  mas/yr  e_pml     Standard deviation in pml, ICRS
    #      107  A1    ---     pmb-      Mean proper motion of the cluster in mu_b sign
    #  108-112  F5.2  mas/yr  pmb       Mean proper motion of the cluster in mu_b, ICRS
    #  116-119  F3.2  mas/yr  e_pmb     Standard deviation in pmb, ICRS
    #  121-125  I5    ---     Nc        Estimated number of members in the cluster
    #  127-129  I3    ---     ref1      Source of the mean proper motion determination
    #      134  A1    ---     RV-       Radial Velocity sign
    #  135-140  F5.2  km/s    RV        Radial Velocity
    #  145-149  F5.2  km/s    eRV       Error in Radial Velocity
    #  153-156  I3    ---     N         Number of stars used to determine Radial Velocity
    #  162-165  I4    ---     ref2      Source of the mean radial velocity determination
    #      169  A1    ---     ME-       Metallicity sign
    #  170-174  F5.3  index   ME        Metallicity
    #  178-182  F5.3  index   eME       Error in Metallicity
    #  185-187  I3    ---     Nme       Number of stars used to determine Metallicity
    #  191-198  A8    ---     TrTyp     Trumpler Type determined in the DSS inspection
    # -------------------------------------------------------------------------------------------------
    @classmethod
    def from_line(self, line):
        cluster = Cluster()
        cluster.line = line

        cluster.name = line[0:18].strip()
        cluster.galactic_longitude = line[18:26].strip()
        cluster.galactic_latitude_sign = line[33]
        cluster.galactic_latitude = line[33:40].strip()
        cluster.classification_flag = line[46:48].strip()
        cluster.apparent_diameter_in_arcmin = line[53:58].strip()
        cluster.distance = line[61:66].strip()
        cluster.color_excess_in_bv = line[72:77].strip()
        cluster.age_in_log_t = line[79:85].strip()
        cluster.mean_proper_motion_in_mu_l_sign = line[91]
        cluster.mean_proper_motion_in_mu_l_icrs = line[91:96].strip()
        cluster.standard_deviation_in_pml = line[98:102].strip()
        cluster.mean_proper_motion_in_mu_b_sign = line[107]
        cluster.mean_proper_motion_in_mu_b_icrs = line[107:112].strip()
        cluster.standard_deviation_in_pmb = line[115:119].strip()
        cluster.number_of_members = line[120:125].strip()
        cluster.source_of_the_mean_proper_motion_determination = line[126:129].strip()
        cluster.radial_velocity_sign = line[134]
        cluster.radial_velocity = line[134:140].strip()
        cluster.error_in_radial_velocity = line[144:149].strip()
        cluster.number_of_stars_used_to_determine_radial_velocity = line[152:156].strip()
        cluster.source_of_the_mean_radial_velocity_determination = line[161:165].strip()
        cluster.metallicity_sign = line[169]
        cluster.metallicity = line[169:174].strip()
        cluster.error_in_metallicity = line[177:182].strip()
        cluster.number_of_stars_used_to_determine_metallicity = line[184:187].strip()
        cluster.trumpler_type = line[190:198].strip()

        return cluster

    def glon(self):
        return self.galactic_longitude

    def de_sign(self):
        return self.galactic_latitude_sign

    def glat(self):
        return self.galactic_latitude

    def klass(self):
        return self.classification_flag

    def diam(self):
        return self.apparent_diameter_in_arcmin

    def d(self):
        return self.distance

    def ebv(self):
        return self.color_excess_in_bv

    def age(self):
        return self.age_in_log_t

    def pml_sign(self):
        return self.mean_proper_motion_in_mu_l_sign

    def pml(self):
        return self.mean_proper_motion_in_mu_l_icrs

    def epml(self):
        return self.standard_deviation_in_pml

    def pmb_sign(self):
        return self.mean_proper_motion_in_mu_b_sign

    def pmb(self):
        return self.mean_proper_motion_in_mu_b_icrs

    def epmb(self):
        return self.standard_deviation_in_pmb

    def nc(self):
        return self.number_of_members

    def ref1(self):
        return self.source_of_the_mean_proper_motion_determination

    def rv_sign(self):
        return self.radial_velocity_sign

    def rv(self):
        return self.radial_velocity

    def erv(self):
        return self.error_in_radial_velocity

    def n(self):
        return self.number_of_stars_used_to_determine_radial_velocity

    def ref2(self):
        return self.source_of_the_mean_radial_velocity_determination

    def me_sign(self):
        return self.metallicity_sign

    def me(self):
        return self.metallicity

    def eme(self):
        return self.error_in_metallicity

    def nme(self):
        return self.number_of_stars_used_to_determine_metallicity

    def trtyp(self):
        return self.trumpler_type

    def latitude_with_sign(self):
        return self.galactic_latitude_sign + self.galactic_latitude

    def valid(self):
        return self.radial_velocity and self.age_in_log_t and self.distance and \
          self.galactic_longitude and self.galactic_latitude and \
          self.mean_proper_motion_in_mu_l_icrs and self.mean_proper_motion_in_mu_b_icrs
