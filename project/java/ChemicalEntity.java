package None;

import java.util.List;
import lombok.*;






/**
  Any constitutionally or isotopically distinct atom, molecule, ion, ion pair, radical, radical ion, complex, conformer etc., identifiable as a separately distinguishable entity.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ChemicalEntity  {

  private InChi inchi;
  private InChIKey inchikey;
  private SMILES smiles;
  private IUPACChemicalFormula iupacFormula;

}